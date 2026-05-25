---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lovelorn"
level: "4"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]], [[Lifesense]] (precise) 30 feet"
languages: "Common (Can't speak any language)"
skills:
  - name: Skills
    desc: "Athletics +11, Occultism +8, Stealth +13"
abilityMods: ["+4", "+5", "+3", "-2", "+2", "+3"]
abilities_top:
  - name: "+2 Perception to Sense Motive"
    desc: ""
  - name: "Cynic's Curse"
    desc: "A creature hit by a lovelorn's fangs Strike must attempt a DC 19 [[Will]] save as it grows morose and listless. If the creature would be affected by a [[Calm]] spell, that spell attempts to counteract this curse instead of having its normal effect. <br> - **Critical Success** The target is unaffected. <br> - **Success** For 1 minute, the target can't benefit from helpful emotion effects, but can still be affected by harmful emotion effects. <br> - **Failure** As success, plus the target is [[Fatigued]] for the same duration. <br> - **Critical Failure** As failure, but the curse's effects are permanent."
armorclass:
  - name: AC
    desc: "21; **Fort** +9, **Ref** +13, **Will** +12"
health:
  - name: HP
    desc: "60; void healing; **Immunities** bleed, death effects, disease, mental, paralyzed, poison, unconscious"
abilities_mid:
  - name: "Gloom Aura"
    desc: "60 feet. A lovelorn's presence instills unease and turns the air cold, dark, and stale. Creatures within the aura take a -1 circumstance penalty to saving throws made to resist emotion effects. <br>  <br> If the lovelorn makes a place home for a week or more, that location can become suffused with this magic even outside the lovelorn's aura, lasting until the lovelorn leaves or is destroyed. <br>  <br> > [!danger] Effect: Gloom Aura"
  - name: "Skitter Away"
    desc: "`pf2:r` **Trigger** A creature ends its movement in a space adjacent to the lovelorn <br>  <br> **Effect** The lovelorn Strides or Climbs 10 feet away from the triggering creature. This movement does not trigger reactions."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +13 (`pf2:1`) (finesse), **Damage** 1d6+6 piercing plus 1d6 bleed plus [[Cynics Curse]]"
  - name: "Melee strike"
    desc: "Gory Tendril +13 (`pf2:1`) (agile, finesse), **Damage** 1d4+6 bludgeoning plus [[Grab]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 21, attack +13<br>**2nd** [[Illusory Creature]] (At Will), [[Invisibility]]<br>**1st** [[Fear]], [[Figment]], [[Illusory Object]] (At Will), [[Telekinetic Hand]]"
abilities_bot:
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A particularly macabre form of undead, these spiderlike creatures resemble still-beating hearts with rib bones for legs and tendrils of gore dangling beneath. Their twisted forms hint at their ghastly origin, as these undead form from those who die tragic deaths in service to toxic love: star-crossed lovers who die rather than accept a life apart from one another, rejected suitors whose unrequited affections warp into malice, and other victims of tragic relationships both romantic and otherwise. Any of these might spawn a lovelorn in death, their anguish and fixation on their broken heart causing the organ to animate.

A freshly spawned lovelorn often seeks out those it knew in life, stalking and tormenting them or, in some cases, those around them. In undeath, they gain an understanding of emotions and how to manipulate them, cultivating the misery, anger, and cruelty they thrive upon. Typically, these undead long to enact vengeance upon those they feel drove them to their tragic fates, although in rare cases they may instead act as dark guardians, fixating on a particular loved one and "protecting" them by visiting misery upon anyone who slights them.

```statblock
creature: "Lovelorn"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
