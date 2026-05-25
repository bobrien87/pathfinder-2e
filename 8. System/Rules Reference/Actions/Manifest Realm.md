---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Divine]]", "[[Manipulate]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per hour

**Effect** You corrupt the surrounding area into a manifestation of your realm in a @Template[type:burst|distance:20]{20-foot-radius burst} centered on you. Your manifested realm counts as difficult terrain for your enemies, and your enemies take a –1 penalty to Fortitude saving throws while in your manifested realm.

> [!danger] Effect: Manifest Realm

You can Sustain your manifested realm once per round on subsequent rounds, and if you do not, the radius of your manifested realm is reduced by 5 feet.

Your realm remains manifested for a maximum of 1 minute, and you can Dismiss your manifested realm. If your manifested realm's radius is ever reduced to 0 feet or if you move beyond 100 feet from the borders of your manifested realm, your manifested realm is automatically Dismissed.

**Source:** `= this.source` (`= this.source-type`)
