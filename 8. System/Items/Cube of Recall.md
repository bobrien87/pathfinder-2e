---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Magical]]"]
price: "{'gp': 40000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small cube has smooth matte sides. One side is black, the opposite side is white, and the other four are various shades of gray. Each side can be attuned to a location and then teleport you back to that spot in the blink of an eye.

**Activate** 10 minutes (concentrate, manipulate)

**Effect** Pick one side of the cube and set it face up. You attune the cube to the location you currently occupy. Each side can be attuned to only one location. Once you use this action to attune to a location, the side you pick loses any previously attuned location.

**Activate** `pf2:3` (concentrate, manipulate, teleportation)

**Effect** While speaking a word of command and bringing the location into your mind, you push the corresponding side of the cube. You teleport to the location attuned to the side you press, within 100 feet of the attuned location, as long as that location is on the same planet. If it's not, your activation produces no effect, but the attunement remains.

**Source:** `= this.source` (`= this.source-type`)
