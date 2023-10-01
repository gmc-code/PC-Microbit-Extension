'\nmicropython module for the Kitronik :MOVE Motor buggy v3.1\nfor microbit, v2\nMOVEMotor module for motors, line following and distance sensing\nGMC-code; 2023\n'
from microbit import pin1,pin2,pin12,pin13,pin14,sleep
import machine
import utime
from neopixel import NeoPixel
RIGHT_LINE_SENSOR_PIN=pin1
LEFT_LINE_SENSOR_PIN=pin2
TRIGGER_PIN=pin14
ECHO_PIN=pin13
class MOVEMotorMotors:
	def __init__(self):self.ws2811=NeoPixel(pin12,2)
	def stop_left(self,brightness=255):self.ws2811[1]=0,0,brightness;self.ws2811.show()
	def stop_right(self,brightness=255):self.ws2811[0]=0,0,brightness;self.ws2811.show()
	def stop(self,brightness=255):self.stop_left(brightness);self.stop_right(brightness)
	@staticmethod
	def _analog_speed(speed):
		if speed<0 and speed>=-10:return int(speed*-21+45)
		elif speed>0 and speed<=10:return int(speed*21+45)
		else:return 0
	def left_motor(self,speed=1,duration=None):
		mB=bytearray([0,0,0]);mJ=bytearray([0,0,0]);motor_speed=self._analog_speed(speed);wsIndex=1
		if speed>0:mB[0]=motor_speed;mJ[0]=255
		else:mB[1]=motor_speed;mJ[1]=255
		self.ws2811[wsIndex]=mJ[0],mJ[1],mJ[2];self.ws2811.show();sleep(1);self.ws2811[wsIndex]=mB[0],mB[1],mB[2];self.ws2811.show()
		if duration is not None:utime.sleep_ms(duration);self.stop_left()
	def right_motor(self,speed=1,duration=None):
		mB=bytearray([0,0,0]);mJ=bytearray([0,0,0]);motor_speed=self._analog_speed(speed);wsIndex=0
		if speed>0:mB[1]=motor_speed;mJ[1]=255
		else:mB[0]=motor_speed;mJ[0]=255
		self.ws2811[wsIndex]=mJ[0],mJ[1],mJ[2];self.ws2811.show();sleep(1);self.ws2811[wsIndex]=mB[0],mB[1],mB[2];self.ws2811.show()
		if duration is not None:utime.sleep_ms(duration);self.stop_left()
	@staticmethod
	def _straight_line_adjustment(analog_speed,adjustment):
		if adjustment<0:adjustment=0
		elif adjustment>20:adjustment=20
		return int(analog_speed*(255-adjustment)/255)
	def backwards(self,speed=1,duration=None,decrease_left=0,decrease_right=0):
		analog_speed=abs(self._analog_speed(speed));mB=bytearray([0,0,0]);mJ=bytearray([0,0,0]);right_speed=self._straight_line_adjustment(analog_speed,decrease_right);left_speed=self._straight_line_adjustment(analog_speed,decrease_left);mJ[0]=255;self.ws2811[0]=mJ[0],mJ[1],mJ[2];mJ[0]=0;mJ[1]=255;self.ws2811[1]=mJ[0],mJ[1],mJ[2];self.ws2811.show();sleep(1);mB[0]=right_speed;self.ws2811[0]=mB[0],mB[1],mB[2];mB[0]=0;mB[1]=left_speed;self.ws2811[1]=mB[0],mB[1],mB[2];self.ws2811.show()
		if duration is not None:utime.sleep_ms(duration);self.stop()
	def forwards(self,speed=1,duration=None,decrease_left=0,decrease_right=0):
		analog_speed=abs(self._analog_speed(speed));mB=bytearray([0,0,0]);mJ=bytearray([0,0,0]);right_speed=self._straight_line_adjustment(analog_speed,decrease_right);left_speed=self._straight_line_adjustment(analog_speed,decrease_left);mJ[1]=255;self.ws2811[0]=mJ[0],mJ[1],mJ[2];mJ[0]=255;mJ[1]=0;self.ws2811[1]=mJ[0],mJ[1],mJ[2];self.ws2811.show();sleep(1);mB[1]=right_speed;self.ws2811[0]=mB[0],mB[1],mB[2];mB[0]=left_speed;mB[1]=0;self.ws2811[1]=mB[0],mB[1],mB[2];self.ws2811.show()
		if duration is not None:utime.sleep_ms(duration);self.stop()
	@staticmethod
	def _turn_radius_factor(radius=25):
		if radius<4:radius=4
		elif radius>800:radius=800
		return(radius+8.5)/radius
	def left(self,speed=1,radius=25,duration=None):
		motor_speed=self._analog_speed(speed);turn_radius_factor=self._turn_radius_factor(radius);motor_speed_inner=int(motor_speed/turn_radius_factor);right_mB=bytearray([0,0,0]);right_mJ=bytearray([0,0,0]);left_mB=bytearray([0,0,0]);left_mJ=bytearray([0,0,0])
		if speed>0:right_mB[1]=motor_speed;right_mJ[1]=255;left_mB[0]=motor_speed_inner;left_mJ[0]=255
		else:right_mB[0]=motor_speed;right_mJ[0]=255;left_mB[1]=motor_speed_inner;left_mJ[1]=255
		self.ws2811[0]=right_mJ[0],right_mJ[1],right_mJ[2];self.ws2811[1]=left_mJ[0],left_mJ[1],left_mJ[2];self.ws2811.show();sleep(1);self.ws2811[0]=right_mB[0],right_mB[1],right_mB[2];self.ws2811[1]=left_mB[0],left_mB[1],left_mB[2];self.ws2811.show()
		if duration is not None:utime.sleep_ms(duration);self.stop_left()
	def right(self,speed=1,radius=25,duration=None):
		motor_speed=self._analog_speed(speed);turn_radius_factor=self._turn_radius_factor(radius);motor_speed_inner=int(motor_speed/turn_radius_factor);right_mB=bytearray([0,0,0]);right_mJ=bytearray([0,0,0]);left_mB=bytearray([0,0,0]);left_mJ=bytearray([0,0,0])
		if speed>0:right_mB[1]=motor_speed_inner;right_mJ[1]=255;left_mB[0]=motor_speed;left_mJ[0]=255
		else:right_mB[0]=motor_speed_inner;right_mJ[0]=255;left_mB[1]=motor_speed;left_mJ[1]=255
		self.ws2811[0]=right_mJ[0],right_mJ[1],right_mJ[2];self.ws2811[1]=left_mJ[0],left_mJ[1],left_mJ[2];self.ws2811.show();sleep(1);self.ws2811[0]=right_mB[0],right_mB[1],right_mB[2];self.ws2811[1]=left_mB[0],left_mB[1],left_mB[2];self.ws2811.show()
		if duration is not None:utime.sleep_ms(duration);self.stop()
	def spin_left(self,speed=1,duration=None):
		analog_speed=abs(self._analog_speed(speed));right_mB=bytearray([0,0,0]);right_mJ=bytearray([0,0,0]);left_mB=bytearray([0,0,0]);left_mJ=bytearray([0,0,0]);right_mB[1]=analog_speed;right_mJ[1]=255;left_mB[1]=analog_speed;left_mJ[1]=255;self.ws2811[0]=right_mJ[0],right_mJ[1],right_mJ[2];self.ws2811[1]=left_mJ[0],left_mJ[1],left_mJ[2];self.ws2811.show();sleep(1);self.ws2811[0]=right_mB[0],right_mB[1],right_mB[2];self.ws2811[1]=left_mB[0],left_mB[1],left_mB[2];self.ws2811.show()
		if duration is not None:utime.sleep_ms(duration);self.stop()
	def spin_right(self,speed=1,duration=None):
		analog_speed=abs(self._analog_speed(speed));right_mB=bytearray([0,0,0]);right_mJ=bytearray([0,0,0]);left_mB=bytearray([0,0,0]);left_mJ=bytearray([0,0,0]);right_mB[0]=analog_speed;right_mJ[0]=255;left_mB[0]=analog_speed;left_mJ[0]=255;self.ws2811[0]=right_mJ[0],right_mJ[1],right_mJ[2];self.ws2811[1]=left_mJ[0],left_mJ[1],left_mJ[2];self.ws2811.show();sleep(1);self.ws2811[0]=right_mB[0],right_mB[1],right_mB[2];self.ws2811[1]=left_mB[0],left_mB[1],left_mB[2];self.ws2811.show()
		if duration is not None:utime.sleep_ms(duration);self.stop()
class MOVEMotorLineSensors:
	def __init__(self):self.left_offset=0;self.right_offset=0
	def line_sensor_calibrate(self):
		rightLineSensor=RIGHT_LINE_SENSOR_PIN.read_analog();leftLineSensor=LEFT_LINE_SENSOR_PIN.read_analog();offset=int(abs(rightLineSensor-leftLineSensor)/2)
		if leftLineSensor>rightLineSensor:self.left_offset=-offset;self.right_offset=offset
		else:self.left_offset=offset;self.right_offset=-offset
	def line_sensor_read(self,sensor):
		if sensor=='left':return LEFT_LINE_SENSOR_PIN.read_analog()+self.left_offset
		elif sensor=='right':return RIGHT_LINE_SENSOR_PIN.read_analog()+self.right_offset
class MOVEMotorDistanceSensors:
	def distance(self):
		ECHO_PIN.set_pull(ECHO_PIN.NO_PULL);TRIGGER_PIN.write_digital(0);utime.sleep_us(2);TRIGGER_PIN.write_digital(1);utime.sleep_us(10);TRIGGER_PIN.write_digital(0);distance=machine.time_pulse_us(ECHO_PIN,1,1160000)
		if distance>0:return round(distance/58)
		else:return 0