---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Concussive]]", "[[Fatal d8]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking flintlock pistol* has the odd construction of possessing two triggers, one of soapstone and one of onyx, clearly separated with individual trigger guards. Originally created by a student at Blythir College in Alkenstar, the mountebank's passage has the ability to create temporary linked portals on existing surfaces. The weapon disappeared shortly after its invention, but rumors have circulated that it now belongs to a group of thieves who use it to commit impossible robberies.

**Activate—Doorway to Onyx** `pf2:1` (manipulate)

**Requirements** the *mountebank's passage* isn't loaded

**Effect** You pull the soapstone trigger. Choose a vertical surface within 120 feet. A beam of white energy crackles to the vertical surface and creates a white portal on that surface. Any creature who moves through the white portal comes out through the mountebank's passage's black portal, if one exists on the same plane. Using this activation causes any previous white portal to disappear, even if you don't create a new portal; otherwise, the portal lasts until your next daily preparations.

**Activate—Doorway to Pearl** `pf2:1` (manipulate)

**Requirements** the *mountebank's passage* isn't loaded

**Effect** You pull the onyx trigger. Choose a vertical surface within 120 feet. A beam of black energy leaps to the surface and creates an onyx portal. Any creature who moves through the black portal comes out through the mountebank's passage's white portal, if one exists on the same plane. Using this activation causes any previous black portal to disappear; even if you don't create a new portal; otherwise, the portal lasts until your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
