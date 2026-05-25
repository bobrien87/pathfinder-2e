---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Light]]", "[[Magical]]", "[[Missive]]"]
price: "{'gp': 20}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate, manipulate)

A glimmering missive sparkles as you compose it. When activated, it explodes, disintegrating into a shower of multicolored motes in a @Template[burst|distance:10] from a corner of the missive's space. Creatures in the area are covered in sparkling dust that remains luminous for 1 hour. Visible creatures can't be [[Concealed]] while covered by the luminous dust; any [[Invisible]] creatures are concealed while covered in the luminous dust, rather than being undetected.

**Source:** `= this.source` (`= this.source-type`)
