---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Clockwork]]"]
price: "{'gp': 15}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A clockwork megaphone uses cunning clockwork gears to adjust the shape and angle of the cone within the megaphone, allowing you to raise or lower the volume, widen or contract the angle in which you project your voice, or both at the same time. This makes a clockwork megaphone far more useful than an ordinary megaphone for situations where you want to make sure that everyone in a particular venue or location can hear you without being so loud that your voice comes across as a painful shout. It takes 1 minute to wind up a clockwork megaphone, which allows it to remain active for up to 1 hour of adjustments, only counting the time you change the megaphone's settings, not the time you spend speaking. Since it automatically enters standby mode when not in use, this typically means you don't have to wind up the clockwork megaphone for months, or even years, depending on how often you adjust the settings each day.

**Source:** `= this.source` (`= this.source-type`)
