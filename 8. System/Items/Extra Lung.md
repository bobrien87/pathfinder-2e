---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Air]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 500}"
usage: "worn"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An *extra lung* is a waterproofed bladder of air worn in an underarm holster, connected to the wearer's nose by a long tube. You can use it as a source of air instead of breathing in the air around you. It can hold 5 rounds' worth of breathable air, and can be refilled if the *extra lung* is left open for 10 minutes in an environment with suitable air.

You can switch to breathing from the *extra lung* at any time, without using an action. You can use air from the bladder following the rules for holding your breath, but you can speak without losing the air from the *extra lung*. When you lose air at the end of each of your turns, choose whether you use breath you're holding or air from the *extra lung*. Speaking causes you to lose breath you're holding but doesn't affect the air in the *extra lung*.

**Activate—Cough Up** R (manipulate)

**Trigger** You breathe in an inhaled poison or other inhaled affliction

**Effect** You cough the poison or tainted air into your *extra lung*, immediately attempting a new save against the effect. The air inside your *extra lung* becomes fouled, and you re-expose yourself to the inhaled affliction if you breathe it in. The *extra lung* is cleansed of any poison it contains every day at dawn.

**Source:** `= this.source` (`= this.source-type`)
