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

Duskwood is a very lightweight wood found primarily in old-growth forests in south-central Avistan; it is dark as ebony but has a slight purple tint. A duskwood item's Bulk is reduced by 1 (or to light Bulk if its normal Bulk is 1, with no effect on an item that normally has light Bulk). The Price of an item made of duskwood is based on the item's normal Bulk, not its reduced Bulk for being made of duskwood, but reduce the Bulk before making any further Bulk adjustments for the size of the item.

Duskwood Items

Duskwood Items
Hardness
HP
BT

**Thin Items**
 
 
 

Standard-grade
5
20
10

High-grade
8
32
16

**Items**
 
 
 

Standard-grade
7
28
14

High-grade
10
40
20

**Structure**
 
 
 

Standard-grade
14
56
28

High-grade
20
80
40

**Source:** `= this.source` (`= this.source-type`)
