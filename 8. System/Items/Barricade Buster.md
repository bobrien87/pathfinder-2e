---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Kickback]]", "[[Orc]]", "[[Razing]]", "[[Repeating]]", "[[Volley 20]]"]
price: "{'gp': 9}"
usage: "held-in-two-hands"
bulk: "3"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Developed by a dromaar inventor from Alkenstar who brought the technology north to battle the Whispering Tyrant alongside the orc hordes of Belkzen, the barricade buster features eight barrels fixed around a central pivot attached to a handle and firing mechanism. A barricade buster fires spheres of metal with extreme velocity and very little accuracy.

**Source:** `= this.source` (`= this.source-type`)
