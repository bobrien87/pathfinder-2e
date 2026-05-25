---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Backswing]]", "[[Disarm]]", "[[Force]]", "[[Monk]]", "[[Parry]]"]
price: "{'gp': 4200}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking impactful sansetsukon* is made of metal colored pale blue that echoes howling winds when swung and emits the force of a storm when it connects.

**Activate—Sonic Gale** `pf2:r` (concentrate, force, magical)

**Trigger** You critically hit with the *twisting gale*

**Frequency** once per 10 minutes

**Effect** The energy of your follow-through erupts from your opponent in a wave of concussive energy. You deal sonic damage equal to your normal Strike damage with the twisting gale in a @Template[cone|distance:30] behind your target. Creatures in the area, not including your target, must attempt a [[Fortitude]] save against your class DC.

**Source:** `= this.source` (`= this.source-type`)
