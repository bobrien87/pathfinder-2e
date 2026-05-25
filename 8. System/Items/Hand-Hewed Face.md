---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Contract]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "other"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

At the crossroads under a new moon, you traded your face for one that you can mold as though it were clay, sealed with a ribbon worn around your neck to hide the seam. Your true appearance changes to that of a generic member of your ancestry. You can shape your facial features with your hands and thus don't need a disguise kit to Impersonate, and you don't take circumstance penalties to Impersonate someone due to the difference in your facial features. Once per day, from any distance, the entity that holds your *bargained contract* can change their appearance to match your appearance from before you sealed the contract, or the appearance you're currently using through Impersonate. When they do, your face transforms to your new true appearance—that of a generic member of your ancestry—and you become [[Stunned]] 3 by the sudden backlash.

**Activate—Fresh Face** `pf2:2` (manipulate)

**Requirements** You have used Impersonate and molded your face into a different face

**Effect** You peel your current face from your skin, revealing the true generic appearance from your *bargained contract*. This allows you to duck out of sight and remove the facial component of your disguise almost immediately, though clothing or other elements might still give you away.

**Source:** `= this.source` (`= this.source-type`)
