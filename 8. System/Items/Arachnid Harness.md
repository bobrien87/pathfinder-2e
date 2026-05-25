---
type: item
source-type: "Remaster"
level: "7"
price: "{'gp': 360}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 leather armor* has four knobbed ribs that wrap around the torso. The armor grants you resistance 2 to poison damage.

**Activate** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** The ribs from the armor spread into functional spider limbs. For 1 minute, you gain a climb Speed equal to half your land Speed and have your limbs free as you climb. If you use all your free limbs to help you Climb, your climb Speed equals your land Speed.

> [!danger] Effect: Arachnid Harness

**Requirements** The initial raw materials must include four intact legs from a giant tarantula.

**Source:** `= this.source` (`= this.source-type`)
