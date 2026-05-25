---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Consumable]]", "[[Cursed]]", "[[Primal]]"]
price: "{'per': 1, 'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

*Bower fruit* got its name from its association with the Green Mother, a fey Eldest with a fondness for plants and manipulation, whose domain is known as the Hanging Bower. She uses these cursed fruits to keep mortals in her thrall, but it's unknown whether she created them or simply popularized their use.

A *bower fruit* condemns a non-fey who tastes it to never again be satisfied with the fare found in the mundane Universe. Any fruit can be cursed in this manner, but stone fruits such as peaches, plums, mangoes, and lychees are most common. Upon activating a *bower fruit* by eating it, you're afflicted with the curse of decadence. You can't recover from stage 1 of the curse naturally, even if you succeed at the save to do so.

**Curse of Decadence** (curse)

**Saving Throw** DC 30 [[Fortitude]] save

**Stage 1** You're afflicted by hunger as if you hadn't eaten food in days. You become [[Fatigued]] and take 1d4 untyped damage each day that can't be healed until you sate your hunger. No amount of eating food can sate your hunger during the spell's duration, with one exception—food from the First World sates your hunger and suppresses the effects, but permanently increases the save DC by 1 (to a maximum of DC 35). After the week ends, if your hunger is still not sated, you take damage from starvation. (1 week)

**Stage 2** As stage 1, plus you're [[Sickened]] 1

**Stage 3** As stage 1, plus you're [[Drained]] 1 and sickened 1

**Stage 4** As stage 1, plus you're [[Drained]] 2, [[Sickened]] 2, and [[Stupefied 2]].

**Source:** `= this.source` (`= this.source-type`)
