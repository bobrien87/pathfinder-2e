---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Auditory]]", "[[Invested]]", "[[Magical]]", "[[Void]]"]
price: "{'gp': 700}"
usage: "wornmask"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ice-blue half-mask is adorned with a wicked silver grin that covers the wearer's mouth, leaving the rest of the face uncovered. You gain a +2 item bonus to Intimidation checks.

**Activate—Hideous Wail** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** The mask emits a soul-chilling scream that deals @Damage[6d10[void]|options:area-damage] damage to each living creature in a @Template[emanation|distance:20] (DC 25 [[Fortitude]] save).

**Craft Requirements** Supply a casting of [[Wails of the Damned]].

**Source:** `= this.source` (`= this.source-type`)
