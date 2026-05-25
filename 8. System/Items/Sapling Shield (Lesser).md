---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]"]
price: "{'gp': 240}"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This surprisingly weighty, though well-balanced, wooden buckler (Hardness 6, HP 48, and BT 24) is emblazoned with the image of a sapling. The sapling withers as the shield takes damage.

**Activate** `pf2:1` (concentrate)

**Effect** The buckler expands, with the sapling image growing into a mighty oak tree. The buckler becomes a tower shield, gaining the corresponding AC bonus, Speed penalty, and ability to [[Take Cover]]. It keeps the same Hit Points and Broken Threshold, but its Hardness and Bulk increase by 2 in this form. The shield remains in this form until you Activate it again to revert it to a buckler.

**Source:** `= this.source` (`= this.source-type`)
