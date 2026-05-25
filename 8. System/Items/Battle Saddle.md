---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Parry]]", "[[Sweep]]", "[[Vehicular]]"]
price: "{'gp': 6}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The battle saddle is a special saddle for a mount that has two large, winglike blades. These blades normally lie flat alongside the saddle, providing additional protection for the rider, but they can be deployed with a tug on the reins to slash at enemies adjacent to the mount. When using a battle saddle to parry, you can decide whether the circumstance bonus to AC applies to you or to your mount.

**Source:** `= this.source` (`= this.source-type`)
