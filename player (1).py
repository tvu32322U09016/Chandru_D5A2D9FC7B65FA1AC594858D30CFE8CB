class player:
  def play(self):
    print("The player is playing cricket.")
class Batsman(player):
  def play(self):
    print("The batsman is batting.")
class Bowler(player):
  def play (self):
    print("The bowler is bowling ")
cricket=player()
batsmen=Batsman()
bowler=Bowler()
cricket.play()
batsmen.play()
bowler.play()
