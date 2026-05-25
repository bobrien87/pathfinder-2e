---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Divine]]", "[[Focused]]", "[[Invested]]"]
price: "{'gp': 1200}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Patterns themed to your curse cover your *oracular crown*. As your curse worsens, the appearance of the crown changes, introducing extreme angles, stronger colors, or other indications of the intensity of your curse. Similarly, it gets closer to its natural form when you reduce the effects of your curse. You gain a +2 item bonus to Religion checks.

**Activate** `pf2:f` envision

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can use only to cast an oracle revelation spell. If not used by the end of your turn, this Focus Point is lost.

**Activate** `pf2:1` (concentrate, healing, vitality)

**Frequency** once per day

**Requirements** Your cursebound value is 1 or higher

**Effect** You regain 3d8 Hit Points. The amount of healing increases to 5d8 if you're cursebound 2, 7d8 if you're cursebound 3, or 9d8 if you're cursebound 4. If you have the void healing ability, this activation has the void trait instead of the healing and vitality traits.

**Craft Requirements** You are an oracle.

**Source:** `= this.source` (`= this.source-type`)
