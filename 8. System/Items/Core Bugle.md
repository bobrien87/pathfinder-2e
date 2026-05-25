---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]"]
price: "{'gp': 1800}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This brass horn is marked by age but remains in excellent condition. The rim of the mouth is ringed by finely carved runes. This bugle grants you a +2 item bonus to Performance checks while playing music with the instrument.

**Activate—Reveille** `pf2:1` (auditory, manipulate)

**Frequency** once per day

**Effect** You blow a swift cadence of sharp notes that carries through the air. You and all allies within a @Template[type:emanation|distance:30] can immediately Stand as a free action; this doesn't provoke reactions.

**Source:** `= this.source` (`= this.source-type`)
