---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Reach]]", "[[Versatile s]]"]
price: "{'gp': 475}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Functioning as a *+1 striking halberd* when wielded as a weapon, a *doomsweeper* is a heavy steel rake-like implement commonly used by frontline soldiers to scour the battlefield for unseen dangers. When you hold a *doomsweeper* extended in front of you, you gain a +1 item bonus to Perception checks to notice any [[Hidden]] hazards in a @Template[type:cone|distance:30], with the bonus increasing to +2 if you are performing the [[Scout]] or [[Search]] exploration action.

**Activate—Clear the Way** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Requirements** You're holding the doomsweeper in 2 hands

**Effect** The *doomsweeper* sweeps the ground clear of obstacles in a @Template[type:cone|distance:30]. This automatically removes any mundane effects of 4th level or lower that would hinder ground movement through the area of effect, including caltrops and non-magical difficult terrain features no deeper or higher than 4 feet. It also attempts to counteract any magical dangers or obstacles with a +14 modifier and a counteract rank of 4th. Finally, it attempts a Thievery check with a +14 modifier to disable all non-magical hazards (but not haunts) in the area. You don't need to be aware of any hazards or effects in the area for the doomsweeper to remove them, but you don't become aware of them if the attempt fails.

**Source:** `= this.source` (`= this.source-type`)
