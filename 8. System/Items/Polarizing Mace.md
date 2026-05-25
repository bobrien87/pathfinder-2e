---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Agile]]", "[[Finesse]]", "[[Shove]]"]
price: "{'gp': 950}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Even grasping the amber handle of this *+1 striking shock light mace* makes your hair stand on end.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Requirements** The wielder of a *grounding spike* is within 30 feet

**Effect** A great surge of electricity connects your paired weapons. All creatures in a line between you and the wielder of the *grounding spike* take @Damage[4d12[electricity]|options:area-damage] (DC 24 [[Reflex]] save).

**Special** The polarizing mace pairs with the *[[Grounding Spike]]*.

**Source:** `= this.source` (`= this.source-type`)
