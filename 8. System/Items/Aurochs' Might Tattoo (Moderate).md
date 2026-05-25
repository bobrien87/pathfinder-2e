---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 2575}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder #207: The Resurrection Flood"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The aurochs depicted by this tattoo is a powerful symbol of strength and resilience. When upgraded, the tattoo expands to depict an increasingly imposing herd of aurochs.

**Activate—Aurochs Charge** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You Stride twice and make a melee Strike against a creature within your reach at any point during your movement. If the Strike hits and deals damage, the target attempts a DC 30 [[Fortitude]] save to avoid being toppled by the impact.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Off Guard]] until the beginning of its next turn.
- **Failure** The target is knocked [[Prone]].
- **Critical Failure** As failure, but the target also takes 4d6 bludgeoning damage.

**Source:** `= this.source` (`= this.source-type`)
