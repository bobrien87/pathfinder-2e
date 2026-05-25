---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 2200}"
usage: "wornbracers"
bulk: "L"
source: "Pathfinder #209: Destroyer's Doom"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These simple bracers look plain on the exterior, but a series of small, sharp studs line the interior like rows of shark teeth. While these bracers are worn and invested, you gain a +2 item bonus to Will saves.

**Activate—Sharp Focus** `pf2:f` (concentrate)

**Trigger** You gain an effect that makes you [[Immobilized]], [[Slowed]], [[Stupefied]], or [[Paralyzed]]

**Effect** Your bracers snap tight onto your wrists, driving the studs into your skin to shock you into focus. You can attempt to counteract the effect causing your condition, with a counteract rank of 6th and a counteract modifier of +22. On a success, you lose the condition. If you have more than one condition from the same source, you only need one counteract check against them.

**Source:** `= this.source` (`= this.source-type`)
