---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Divine]]", "[[Focused]]", "[[Invested]]"]
price: "{'gp': 6000}"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The most devoted, cloistered clerics wear a *cloister robe*. Decorations symbolic of a specific deity adorn the robe, and the robe's colors and the complexity of its construction fit the deity's outlook. The robe serves as a religious symbol of that deity, and it doesn't need to be wielded to provide that benefit.

The robe is *+2 greater resilient explorer's clothing* and grants a +2 item bonus to Religion checks. The robe doesn't grant any benefits to a wearer who doesn't worship the deity tied to the robe. In addition, when you cast a domain spell from one of the deity's domains, you gain resistance to damage from divine spells until the end of your next turn. This resistance is equal to half the robe's level.

> [!danger] Effect: Cloister Robe

**Activate—Domain Devotion** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** Gain 1 Focus Point, which you can spend only to cast a cleric domain spell for a domain belonging to the deity the vestments are dedicated to. If you don't spend this point by the end of this turn, it is lost.

**Craft Requirements** You are a cleric who worships the deity tied to the robe.

**Source:** `= this.source` (`= this.source-type`)
