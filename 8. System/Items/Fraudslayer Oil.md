---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Contact]]", "[[Mental]]", "[[Poison]]"]
price: "{'gp': 650}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:3` (manipulate)

Made from a rare root that reacts to the physical changes that happen when someone is being deceitful, fraudslayer oil is a blunt instrument. It can compel truth, but it carries a fatal price if the victim can't stop themself from repeatedly telling lies. While under the effect of fraudslayer oil, the victim takes the listed poison damage and mental damage for any time they voluntarily and knowingly tell a lie, due to the poison's increased blood pressure to their brain. They take this damage once per round at most, even if they lie several times in rapid succession. The victim is aware of this effect and can choose to not answer or give only evasive, technically truthful, answers.

**Saving Throw** DC 34 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 6 minutes

**Stage 1** [[Stupefied 1]], 3d6 poison damage and 3d6 mental damage for lying (1 minute)

**Stage 2** [[Stupefied 2]], 4d6 poison damage and 4d6 mental damage for lying (1 minute)

**Stage 3** [[Stupefied 3]], 5d6 poison damage and 5d6 mental damage for lying, and the damage becomes a death effect. If it reduces the victim to 0 Hit Points, the victim's head explodes, causing death (1 minute).

**Source:** `= this.source` (`= this.source-type`)
