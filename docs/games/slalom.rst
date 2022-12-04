====================================================
Slalom
====================================================


| Slalom https://the.computing.cafe/add868/slalom-with-micro%3abit-and-micropython
| Tilt to move side to side so moving wall is not hit.


.. code-block:: python

    import microbit as m
    import random

    p = m.display.show

    min_x = -1024
    max_x = 1024
    range_x = max_x - min_x

    wall_min_speed = 500
    player_min_speed = 300

    wall_max_speed = 150
    player_max_speed = 50

    speed_max = 12


    while True:

        i = m.Image("00000:" * 5)
        s = i.set_pixel

        player_x = 2

        wall_y = -1
        hole = 0

        score = 0
        handled_this_wall = False

        wall_speed = wall_min_speed
        player_speed = player_min_speed

        wall_next = 0
        player_next = 0

        while True:
            t = m.running_time()
            player_update = t >= player_next
            wall_update = t >= wall_next
            if not (player_update or wall_update):
                next_event = min(wall_next, player_next)
                delta = next_event - t
                m.sleep(delta)
                continue

            if wall_update:
                # calculate new speeds
                speed = min(score, speed_max)
                wall_speed = wall_min_speed + int(
                    (wall_max_speed - wall_min_speed) * speed / speed_max
                )
                player_speed = player_min_speed + int(
                    (player_max_speed - player_min_speed) * speed / speed_max
                )

                wall_next = t + wall_speed
                if wall_y < 5:
                    # erase old wall
                    use_wall_y = max(wall_y, 0)
                    for wall_x in range(5):
                        if wall_x != hole:
                            s(wall_x, use_wall_y, 0)

            wall_reached_player = wall_y == 4
            if player_update:
                player_next = t + player_speed
                # find new x coord
                x = m.accelerometer.get_x()
                x = min(max(min_x, x), max_x)
                # print("x accel", x)
                s(player_x, 4, 0)  # turn off old pixel
                x = ((x - min_x) / range_x) * 5
                x = min(max(0, x), 4)
                x = int(x + 0.5)
                # print("have", position, "want", x)

                if not handled_this_wall:
                    if player_x < x:
                        player_x += 1
                    elif player_x > x:
                        player_x -= 1
                # print("new", position)
                # print()

            if wall_update:
                # update wall position
                wall_y += 1
                if wall_y == 7:
                    wall_y = -1
                    hole = random.randrange(5)
                    handled_this_wall = False

                if wall_y < 5:
                    # draw new wall
                    use_wall_y = max(wall_y, 0)
                    for wall_x in range(5):
                        if wall_x != hole:
                            s(wall_x, use_wall_y, 6)

            if wall_reached_player and not handled_this_wall:
                handled_this_wall = True
                if player_x != hole:
                    # collision! game over!
                    break
                score += 1

            if player_update:
                s(player_x, 4, 9)  # turn on new pixel

            p(i)

        p(i.SAD)
        m.sleep(800)
        m.display.scroll("Score:" + str(score), delay=60)

        while True:
            if m.button_a.is_pressed() or m.button_b.is_pressed():
                break
            m.sleep(100)



----

.. admonition:: Tasks

    #. Test the various speed variables to find values for an easy game and for a hard game. Add choice of games via buttons at start.

