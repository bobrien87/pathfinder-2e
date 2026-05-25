---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Invested]]", "[[Magical]]", "[[Unholy]]"]
price: "{'gp': 15000}"
usage: "wornmask"
bulk: "—"
source: "Pathfinder #205: Singer, Stalker, Skinsaw Man"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This unsettling mask is made from different flensed faces that have been stitched together with bright red thread. Wearing a *soulfeeding mask* allows you to see others' souls within their bodies as long as they're within 60 feet, as if under the effects of see the unseen and truesight (but only against living or undead creatures). Your Perception DC increases by 10 against living creatures who Impersonate undead creatures or against undead creatures who Impersonate living creatures, as you can tell if the creature's soul has been affected by undeath. The *soulfeeding mask* counteract rank is 9, with a counteract modifier of +31. While wearing a *soulfeeding mask*, you gain darkvision. If you're holy, you're [[Enfeebled]] 2 while you have a *soulfeeding mask* invested.

**Activate—Devour Soul** `pf2:2` (concentrate, death, void)

**Frequency** once per day

**Effect** The *soulfeeding mask*'s eyes and jaw open wide, and clouds of darkness and shadow spill out and attempt to engulf a single creature you can see that's within 30 feet. That creature takes 50 void damage with a DC 36 [[Fortitude]] save. If the target is undead or otherwise has void healing, this activation loses the death and void traits and gains the vitality trait, and the target takes 50 vitality damage with a DC 36 [[Fortitude]] save. If the target takes any damage, you become [[Quickened]] 1 for 1 minute and can use the extra action each round for only Stride actions, unless the damage killed the creature, in which case you can also use the extra action each round for Strike actions as well.

**Activate—Disgorge Soul** `pf2:3` (concentrate)

**Requirements** You're quickened as a result of Devour Soul

**Effect** The *soulfeeding mask* disgorges the devoured soul. You're no longer quickened from Devour Soul, and the *soulfeeding mask* casts duplicate foe (DC 36 [[Fortitude]] save) to your specifications, targeting the creature whose soul had been devoured. You must Sustain this effect, unless the target creature was slain by Devour Soul, in which case duplicate foe functions as if the creature had failed its save, and the *soulfeeding mask* Sustains this spell automatically.

**Source:** `= this.source` (`= this.source-type`)
