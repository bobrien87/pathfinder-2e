---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Mechanical]]"]
price: "{'gp': 450}"
usage: "worn"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The city of Riddleport is notorious for its noxious air and water. While some inhabitants tolerate the haze, most wear bootstrap respirators to filter out as many of the pollutants as possible. Designed by dwarf smiths operating the Gas Forges, the flexible face mask of a bootstrap respirator fits snugly over your mouth and nose, fastened by two adjustable leather straps. A manual pump inserted into your footwear or under the arm circulates air through tubes and over filters fitted into the front of the mask. While wearing a bootstrap respirator, you gain a +1 item bonus to any saves that require you to smell or taste, such as inhaled poisons and airborne diseases.

**Source:** `= this.source` (`= this.source-type`)
