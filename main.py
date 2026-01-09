def on_a_pressed():
    pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

Mau = sprites.create(assets.image("""
    Mau
    """), SpriteKind.player)

music.play("Kanye West - Flashing Lights ft. Dwele 4.mp3", music.PlaybackMode.UNTIL_DONE)
