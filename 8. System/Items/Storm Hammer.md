---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Electricity]]", "[[Magical]]", "[[Shove]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Beginner Box"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Sparks of crackling electricity arc from this *+1 magic warhammer*, and the head thrums with distant thunder. Any hit with this hammer deals 1 extra electricity damage. You can use a special action to transform the sparks into lightning bolts.

**Activate—Electrify** `pf2:1` (concentrate)

Until the end of your turn, the hammer deals 1d6 extra electricity damage instead of just 1. After you activate the *storm hammer*, you can't activate it again for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
