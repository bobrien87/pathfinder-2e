---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 55}"
usage: "worn"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Many armies recruit musicians among their number, who might keep time for marching with a drum, play out commands with a bugle, or intimidate foes with the bagpipes. Regardless of instrument, these musicians are still soldiers and need to be able to fight as well as play at the drop of a hat. The instrument harness is made from white leather decorated with gold musical symbols. You can attach up to 3 Bulk of musical instruments to the harness. If you drop an attached instrument, it remains safely at your side rather than dropped to the ground.

**Activate—Ready to Play** `pf2:f`

**Frequency** once per day

**Requirements** There is an instrument attached to the instrument harness and you have enough hands free to hold it

**Effect** Your harness ripples, pulling the required instrument into your hands. You Interact to draw the required instrument, but this manipulate action doesn't trigger reactions.

**Source:** `= this.source` (`= this.source-type`)
