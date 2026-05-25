---
type: item
source-type: "Remaster"
level: "1"
traits: "Magical"
price: ""
usage: ""
bulk: "—"
activate: ""
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null, "**Traits** " + this.traits, "")`

`= choice(this.price != null, "**Price** " + this.price, "") + choice(this.usage != null, choice(this.price != null, "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null, choice(this.price != null or this.usage != null, "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null, "**Activate** " + this.activate, "")`

**Frequency** once per round

**Effect** You transform a non-magical arrow or bolt on your person into a piece of magical ammunition of one type you chose for the [[Magic Ammunition]] feat. You must shoot the ammunition before the end of your turn or the magic dissipates. If the ammunition has an Activate entry, you still need to spend the required actions to activate the ammunition before shooting it.

You can choose a type of magical ammunition that is typically not available to the type of ammunition you're using—for example, you can use [[Climbing Bolt]] on an arrow, even though that magical ammunition is normally only found on bolts.

**Source:** `= this.source` (`= this.source-type`)
