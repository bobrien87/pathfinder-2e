---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Concussive]]", "[[Fatal d8]]", "[[Magical]]"]
price: "{'gp': 3000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking flintlock pistol* bears strange, jagged markings of erratic design and has an oddly squishy grip. It can be activated to produce a variety of unusual effects

**Activation—Wonder Shot** `pf2:2` (manipulate)

**Effect** Choose a creature within 60 feet and roll a percentile die on the table below to determine the pistol's effect. If an entry lists a spell, the pistol Casts that Spell at the indicated level (or at its lowest level, if no level is listed). You make any decisions for a spell cast by the pistol unless otherwise indicated, except that it must only target the creature you chose, or the creature you chose must be the center of the spell's area, if it has an area but no targets. The only exception to the limitation on targeting is if the effect specifically states it targets you. If the spell's range is less than 60 feet, increase the range to 60 feet. Any spell DC required is DC 29, and any spell attack modifier required is +21. If the pistol casts a spell on you, you don't get a saving throw or any other defense against it. Once activated, the pistol can't be activated again for 1d4 hours.

d%Wondrous Effect1-2The pistol casts [[Summon Animal]] (3rd rank) to produce a [[Hippogriff]] adjacent to you; only you can ride it.

3The target becomes a shiny metal color (bronze, copper, or iron) and any sound or speech becomes tinny and robotic in nature; this effect lasts 1 month.4-5The pistol casts [[Planar Tether]].6[[Rewrite Memory]] (6th rank) causes the target to forget you ever existed; you can't Sustain the Spell.7-13A short rod protrudes from the pistol and unfurls a small flag that reads "Bang!". The pistol can't be fired until the flag is removed, which requires a single Interact action.14-16You are pushed 30 feet directly away from the target; if you hit an object or creature, you stop, but take falling damage equal to the distance you moved (if you hit a creature, it takes the same amount of falling damage).17-19The target is pushed 30 feet directly away from you; if it hits an object or creature, it stops, but takes falling damage equal to the distance it moved (if it hits another creature, the other creature takes the same amount of falling damage).20You don't need to eat or drink for 1 week.21-25The pistol casts [[Toxic Cloud]].26-30The pistol casts [[Heroism]] on you.31The pistol casts [[One with Plants]] on you, except you appear as a Medium wooden grave marker bearing your name and the current date; you can't Dismiss the spell for 1 round.32The pistol casts [[Mask of Terror]], except the target appears as a more fearsome and violent version of itself to all observers.33-35The target knows you have a bullet with its name on it; the first time you Strike the target with the pistol before the end of your next turn, roll the attack roll twice and take the highest result (this is a fortune effect).36-37The pistol casts [[Cloak of Colors]] on you with a duration of 1d10 rounds.38-47The pistol casts [[Hydraulic Push]] (4th rank) as water streams from the pistol.48-50The pistol casts [[Translocate]] on you, teleporting you to the space adjacent to the target opposite your current position; if that space isn't clear, you instead teleport to the nearest open space.51The pistol casts [[Disintegrate]].52Dozens of tattered, nonmagical playing cards burst from the pistol's barrel.53-54Shadows crowd around the target, making all creatures [[Concealed]] to the target while not in bright light; this effect lasts for 1 hour.55-57Normal vegetation within 30 feet of the target immediately dies and turns to ash.58The pistol casts [[Dinosaur Form]] on you to transform you into a triceratops; the pistol protrudes from the base of your front horn, and you can fire (but not reload) the pistol while in this form.59All non-artifact ammunition in your possession crumbles to dust.60-69You are [[Quickened]] for 1 minute. You can use the extra action only to reload or fire the pistol.70-71The target is [[Quickened]] for 1 minute. It can use the extra action only to Step or Stride.72-79The pistol casts vision of death.

80-81Dozens of bullet holes appear in the target's nonmagical clothing. The effect is purely cosmetic.82-85The pistol casts [[Outcast's Curse]].86The pistol vanishes, reappearing among your possessions once it can be activated again.87-91The pistol casts a 4th-rank mist, but with swirling dust and sand instead of fog.

92-96The pistol casts [[Mountain Resilience]] on you, making your skin rough and leathery; the target ignores the resistance you gain from this spell, and the target's attacks don't reduce the spell's duration.97-99The pistol casts [[Uncontrollable Dance]] with a duration of 3 rounds, even on a failure or critical failure.100Reroll two results and apply both in the order rolled; further results of 100 on these rerolls have no effect.

**Source:** `= this.source` (`= this.source-type`)
