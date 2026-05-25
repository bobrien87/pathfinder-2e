---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]", "[[Wood]]"]
price: "{'gp': 1250}"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *standard-grade duskwood shield* is perfectly symmetrical and incredibly sturdy despite its elaborate construction. These shields are typically given to the chosen emissaries of a kizidhar shuyookh, and the shuyookh's name and title are engraved in Muan behind the shield's handle.

**Activate - Repair** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** You command the shield to repair itself, awakening the restorative magic within. For the next minute, the shield heals 3 Hit Points each round at the start of your turn.

**Activate - Secure Site** 10 minutes (manipulate)

**Frequency** once per day

**Effect** You place the *kizidhar's shield* into the ground at the edge of your campsite, which can't be more than 30 feet on a side, then speak the name of the kizidhar shuyookh carved into its handle. The shuyookh briefly appears just long enough to make a sweeping gesture, causing sprawling thorns to grow in an unnaturally symmetrical formation around the campsite, protecting it for the next 8 hours with an effect that's otherwise identical to [[Wall of Thorns]]. All creatures within the campsite are then immediately affected by a three-action [[Heal]] spell cast at 4th rank by the shield. After 8 hours, the wall rots away, and the shield can be retrieved as an Interact action.

**Source:** `= this.source` (`= this.source-type`)
