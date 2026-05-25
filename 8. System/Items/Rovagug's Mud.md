---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 600}"
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

Rovagug's mud smells and tastes like wet, sour earth. For 1 hour after you drink it, you have a +2 item bonus to saving throws against incapacitation effects. Also, you can use a single action to breathe out a @Template[cone|distance:20] of bitter vapor that causes an earth-shaking rumble that can be heard for 100 feet. Creatures and objects in the area take @Damage[5d6[untyped]|options:area-damage] damage (DC 30 [[Fortitude]] save), decreasing Hardness by 5. An object's Hardness remains lowered for 1d4 rounds, and you can't use this breath again for the same amount of time.

> [!danger] Effect: Rovagug's Mud

**Source:** `= this.source` (`= this.source-type`)
