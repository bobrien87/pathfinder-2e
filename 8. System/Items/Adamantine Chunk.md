---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Precious]]"]
price: "{'gp': 500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Mined from rocks that fell from the heavens, adamantine is one of the hardest metals known. It has a shiny, black appearance, and it is prized for its amazing resiliency and ability to hold an incredibly sharp edge.

Adamantine Items

Adamantine Items
Hardness
HP
BT

**Thin Items**
 
 
 

Standard-grade
10
40
20

High-grade
13
52
26

**Items**
 
 
 

Standard-grade
14
56
28

High-grade
17
68
34

**Structure**
 
 
 

Standard-grade
28
112
56

High-grade
34
136
68

**Source:** `= this.source` (`= this.source-type`)
