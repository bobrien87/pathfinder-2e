---
type: creature
group: ["Aquatic", "Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Water Orm"
level: "10"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Aquatic"
trait_02: "Beast"
trait_03: "Water"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]]"
languages: "Thalassic (Can't speak any language)"
skills:
  - name: Skills
    desc: "Athletics +19, Stealth +23"
abilityMods: ["+8", "+5", "+5", "-3", "+5", "+0"]
abilities_top:
  - name: "Slow Metabolism"
    desc: "A water orm can go for 10 years without feeding. Beyond this limit, the water orm's hunger causes it to become [[Slowed]] 1 but doesn't otherwise impact its lifespan. A water orm that's slowed as a result of starvation can remove this condition by using Swallow Whole to gulp down a meal."
  - name: "Undetectable"
    desc: "A water orm automatically tries to counteract any detection, revelation, or scrying ability attempted against it, using its Stealth modifier for the counteract check."
armorclass:
  - name: AC
    desc: "30; **Fort** +21, **Ref** +19, **Will** +17"
health:
  - name: HP
    desc: "170; **Resistances** cold 10, fire 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +24 (`pf2:1`) (reach 15 ft.), **Damage** 2d10+11 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Tail +24 (`pf2:1`) (agile, reach 15 ft.), **Damage** 2d6+11 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Swallow Whole"
    desc: "`pf2:1` Large, @Damage[(2d8+8)[bludgeoning]] damage, Rupture 22 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Water Travel"
    desc: "`pf2:3` A water orm can dissolve into water, appearing only as a long, dark, serpentine stretch of liquid. While in this form, a water orm's swim Speed increases to 600 feet, it automatically succeeds at Athletics checks to Swim, and it gains a +4 circumstance bonus to Stealth checks in water. A water orm can remain in this form for 8 hours, but it can't enter salt water when using this ability. A water orm can return to its normal form by Dismissing this action."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These legendary creatures lurking in remote lakes always seem to find their way into the tavern tales of lakeside communities. To some travelers, every lake of respectable size seems to be surrounded by towns full of fishers claiming to have spotted a water orm. These elusive creatures inhabit lakes mainly in cool and gloomy regions. Some claim that water orms are an offshoot of sea serpents and linnorms, but no credible link between these creatures has been found.

Water orms have many features that sea serpents don't, such as the ability to understand the rudiments of language. Their natural inclination to avoid contact and remain hidden often remains at odds with their equally compelling curiosity about those they might spy upon the shores of their lakes. Water orm sightings usually occur when they can't help but to rise up to the surface to take a peek at someone (or something) particularly unusual on the beach or floating on the water's surface.

These creatures are extremely long lived and can go for decades, or even centuries, with very little to eat. This allows water orms to subsist in lakes without surfacing for many years, even in bodies of fresh water without ample food sources. Water orms might lie in a silty lake bed for years, their elusiveness only contributing to their mythical reputation. When a pet or child goes missing near a lake, rumors might hold that the local water orm is responsible, leading to folktales that caution residents against venturing out alone near the water.

While most water orms are described as serpentine or long-necked reptiles, others look similar to bizarrely elongated seals or whales, impossibly large sea horses, or long-necked creatures with paddles resembling those of elasmosauruses.

```statblock
creature: "Water Orm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
