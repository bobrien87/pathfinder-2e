---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Deadly d8]]", "[[Jousting d6]]", "[[Magical]]", "[[Reach]]"]
price: "{'gp': 225}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking lance* bears a pennant that displays a standard, heraldry, or other symbols desired by its original creator. When mounted and wielding a *cavalry commander's lance*, you gain a +2 circumstance bonus to Diplomacy checks when interacting with anyone loyal to the nation or cause represented by your pennant's imagery.

**Activate—Ride Them Down!** `pf2:1` (auditory, concentrate, linguistic)

**Frequency** once per day

**Requirements** Your last action was to Strike and inflict damage on a target with the cavalry commander's lance

**Effect** You shout a command to all mounted allies within 60 feet, granting them a +1 circumstance bonus on the next attack roll they make against the target you just damaged before the start of your next turn.

> [!danger] Effect: Ride Them Down!

**Source:** `= this.source` (`= this.source-type`)
