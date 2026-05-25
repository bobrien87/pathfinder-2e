---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Deadly d8]]", "[[Holy]]", "[[Jousting d6]]", "[[Reach]]"]
price: "{'gp': 150}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This white +1 striking lance is made from the horn of a unicorn, willingly granted at the end of its lifetime. Strikes made with this lance gain the holy trait and deal an additional 1 spirit damage. You can make the lance glow like a torch or suppress its light by using an action, which has the concentrate trait.

**Activate** `pf2:2` (magical, manipulate)

**Frequency** once per hour

**Effect** You evoke the spirit of the unicorn that donated the alicorn lance's horn, which you ride in a shining charge. Move up to twice your Speed and make a Strike with the alicorn lance; you gain the effects of the lance's jousting trait on this Strike. If you were already mounted when you Activate the horn, the unicorn spirit takes shape around your steed, granting it a +10–foot status bonus to its Speed for the charge.

**Craft Requirements** The initial raw materials must include a horn willingly gifted by a unicorn. In rare instances, an alicorn lance can be made with a forcibly taken horn. However, this heinous act pollutes the horn's magic, causing it to glow with a sickly red light; remove the holy trait, add the unholy trait to Strikes instead of the holy trait, and make the unicorn spirit evoked in the charge whinny visibly in pain.

**Source:** `= this.source` (`= this.source-type`)
