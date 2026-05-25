---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 30}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This delicately embroidered scarf matches with every outfit and can even complete a costume or disguise with illusions.

**Activate—Masquerade** 1 minute (manipulate)

**Frequency** once per day

**Effect** You arrange the scarf over your lower face, and it casts a 1st-rank [[Illusory Disguise]] spell on you, which ends immediately if the scarf is removed. You can alter the scarf's appearance or make it invisible as part of the *illusory disguise*, but it can still be felt if touched.

**Source:** `= this.source` (`= this.source-type`)
