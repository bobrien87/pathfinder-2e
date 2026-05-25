---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 3000}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This black velvet cloak has a silvery blue iridescent lining. The cloak can be worn with either side facing out—switching from one side to the other requires two Interact actions. If these actions are both taken on the same turn, the act of removing and redonning the cloak doesn't cause it to lose its investiture. When worn with the black velvet lining facing out, the stage magician's cloak grants a +2 item bonus to Occultism checks. When worn with the silvery blue lining facing out, it grants a +2 item bonus to Arcana checks.

**Activate—Now You See Me...** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** Distracting colorful smoke blasts outward from the cloak in a @Template[emanation|distance:10], causing all creatures in the area to become [[Off Guard]] until the start of your next turn (DC 30 [[Will]] save). If you were previously [[Concealed]], [[Hidden]], or undetected, you lose those conditions. You become [[Quickened]] for 1 round and may use the extra action to Interact, Strike, or Stride.

**Activate—...Now You Don't** `pf2:2` (manipulate, teleportation)

**Frequency** once per day

**Effect** Harmless silver smoke issues from the cloak in a @Template[emanation|distance:10]. You cast a 2nd-rank [[Invisibility]] on yourself and are transported, along with all items you're wearing and holding, from your current space to an unoccupied space within 30 feet that you can see. If this would bring another creature with you—even if you're carrying it in an extradimensional space—the transportation part of this effect fails.

**Source:** `= this.source` (`= this.source-type`)
