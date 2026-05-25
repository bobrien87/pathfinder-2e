---
type: item
source-type: "Remaster"
level: "2"
price: "{'gp': 30}"
usage: "worneyepiece"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The darkened lenses of these goggles protect sensitive eyes from bright light but make seeing in the dark more difficult. While wearing day goggles, you gain a +1 item bonus to saving throws against visual light effects. However, while wearing the goggles, you take a -2 item penalty to visual Perception checks and you treat areas of bright light as dim light and areas of dim light as darkness for the purpose of whether you can see. While this is normally a disadvantage, if you have light blindness, you aren't [[Dazzled]] in bright light as long as you continue wearing the day goggles, since to your eyes, there is only dim light. You can wear the goggles around your neck or on your forehead, granting no benefits, but allowing you to move them over your eyes with a single Interact action, without having to withdraw them first.

**Source:** `= this.source` (`= this.source-type`)
