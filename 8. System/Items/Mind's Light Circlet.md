---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Focused]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 1200}"
usage: "wornheadwear"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Gemstones of many colors adorn the silver of a *mind's light circlet*. When you're charged with mental power, the jewels scintillate with light, with different gems resonating based on your emotions. If you have at least 1 Focus Point, the gems cast dim light in a 10-foot radius. When you amp a spell, the light increases to bright light in a 20-foot radius (and dim light to the next 20 feet) until the start of your next turn.

You gain a +2 item bonus to Occultism checks. You also gain the following amp, which you can apply to any of your psi cantrips that have a target or area, much like an amp gained from a feat.

**Amp** You transfer some of the magical luminescence from the mind's light circlet to one of the creatures. Choose a creature targeted by the spell or in its area. Until the start of your next turn, that creature sheds bright light in a 20-foot radius (and dim light to the next 20 feet) and can't be [[Concealed]]. If the creature is [[Invisible]], it's concealed while alight, rather than being undetected.

> [!danger] Effect: Mind's Light Circlet

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can use only to use a psychic amp. If not used by the end of your turn, this Focus Point is lost.

**Craft Requirements** You are a psychic.

**Source:** `= this.source` (`= this.source-type`)
