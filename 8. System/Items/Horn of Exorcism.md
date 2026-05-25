---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]"]
price: "{'gp': 1250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *horn of exorcism* is an instrument made from an animal horn, or an object of the same shape from carved wood or ivory.

**Activate—Rattle the Dead** `pf2:1` (auditory, manipulate)

**Frequency** once per hour

**Effect** Blowing into the horn frightens ghosts and evil spirits who can hear its call. Make an Intimidation check to [[Demoralize]] against all creatures with the undead or unholy trait in a @Template[emanation|distance:30]. This can affect even a mindless creature with that trait, and you don't take a penalty when you attempt to Demoralize a creature that doesn't understand your language.

**Activate—Sacred Seeds** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You fill the horn with sacred seeds and then scatter them around you with a twist of your wrist. The horn grants you and your allies in a @Template[emanation|distance:30] the *ghost touch* property rune on all of your weapon and unarmed Strikes for 1 minute.

> [!danger] Effect: Horn of Exorcism (Sacred Seeds)

**Source:** `= this.source` (`= this.source-type`)
