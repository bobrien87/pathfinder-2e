---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Focused]]", "[[Invested]]", "[[Occult]]"]
price: "{'gp': 13000}"
usage: "wornbelt"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The designs adorning these lush sashes often imitate the decor of famous opera houses, theaters, and museums. When you invest this item, choose Deception, Diplomacy, Intimidation, or Performance; you gain a +3 item bonus to that skill.

**Activate—Encore!** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** Gain 1 Focus Point, which you can spend only to cast a bard composition spell. If you don't spend this point by the end of this turn, it is lost.

**Activate—Transcribe** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You tuck a small roll of paper into the cincture. For the next hour or until you Dismiss the activation, any performance you make is recorded on the paper, and the paper expands as necessary to accommodate it. Depending on the type of performance, this might take the form of sheet music, a transcript, or a diagram of dance moves.

**Craft Requirements** You are a bard.

**Source:** `= this.source` (`= this.source-type`)
