---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Poison]]"]
price: "{'gp': 30}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Sharp and pungent, but tasty, pucker pickles were created by goblin alchemists working to avoid being eaten by larger creatures. For 1 hour after eating a pucker pickle, you smell slightly of pickle, but you have a horrendous taste. Once a creature hits you with a Strike using an attack that allows it to taste you, such as a jaws Strike, it takes a –2 circumstance penalty to further attacks against you that allow it to taste you, including attacks like [[Grappling]] or [[Tripping]] you using its jaws or Swallowing you Whole. Creatures, especially animals, often choose other targets after tasting you. Any creature that Engulfs you or Swallows you Whole is [[Sickened]] 1. If it spends an action retching to reduce the sickened condition, you can attempt to [[Escape]] as a reaction.

> [!danger] Effect: Pucker Pickle

**Source:** `= this.source` (`= this.source-type`)
