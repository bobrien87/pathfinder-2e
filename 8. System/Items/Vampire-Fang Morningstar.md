---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Versatile p]]"]
price: "{'gp': 500}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking wounding morningstar* is studded with teeth pulled from a vampire, which usually requires an animate donor, given vampires' tendency to turn to dust when destroyed.

**Activate** `pf2:1` (manipulate)

**Frequency** once per minute

**Requirements** Your last action was a successful Strike with this weapon and you're not in direct sunlight

**Effect** The *vampire-fang morningstar* absorbs blood from the target, healing the wielder for 10 healing Hit Points.

**Craft Requirements** The initial raw materials must include teeth from a vampire.

**Source:** `= this.source` (`= this.source-type`)
