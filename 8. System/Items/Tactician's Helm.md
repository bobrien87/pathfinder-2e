---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 160}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Repurposing and enchanting a helmet worn by a battlefield commander can create a *tactician's helm*, imparting knowledge of battlefield tactics that feeds off your minor victories. The helm grants you a +1 item bonus to Warfare Lore checks. Also, a jewel adorns the brow of the helmet. This jewel becomes charged each time you hit a creature with a [[Reactive Strike]]. A *tactician's helm* can hold up to 2 charges, and its charges reset to 0 when you invest it.

**Activate** `pf2:1` (concentrate)

**Requirements** The helm's jewel is charged

**Frequency** once per hour

**Effect** One charge in the helm's jewel expires, and you choose one of the following effects.

- **Charge!** Stride twice.
- **Move It!** You gain a +2 status bonus to Acrobatics and Athletics checks until the end of this turn. 

> [!danger] Effect: Tactician's Helm (Move It!)

- **Protect!** If you're wielding a shield, Stride to a space adjacent to an ally, then Raise your Shield.
- **Re-Arm!** Interact up to three times. Each of these actions must be used to do something listed under [[Interact]].

**Source:** `= this.source` (`= this.source-type`)
