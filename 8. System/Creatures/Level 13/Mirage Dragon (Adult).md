---
type: creature
group: ["Arcane", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mirage Dragon (Adult)"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Arcane"
trait_02: "Dragon"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+25; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +25, Arcana +24, Athletics +25, Crafting +24, Deception +29, Diplomacy +27, Performance +27, Stealth +27, Thievery +25, Illusion Lore +26"
abilityMods: ["+6", "+6", "+5", "+5", "+6", "+8"]
abilities_top:
  - name: "Camouflage"
    desc: "The dragon can Hide in natural environments even if they don't have cover."
  - name: "Illusion Sense"
    desc: "When the dragon moves within 30 feet of an illusion that can be disbelieved, they automatically attempt a secret check to disbelieve, even if they didn't spend an action to Interact."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Hallucinatory Breath whenever they score a critical hit with a Strike."
  - name: "Sneak Attack"
    desc: "The dragon's Strikes deal an additional 2d6 precision damage to [[Off Guard]] targets."
armorclass:
  - name: AC
    desc: "33; **Fort** +22, **Ref** +23, **Will** +25"
health:
  - name: HP
    desc: "235; **Immunities** fascinated, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Arcane"
    desc: ""
  - name: "Scintillating Defense"
    desc: "`pf2:r` **Trigger** The dragon is targeted with an attack <br>  <br> **Effect** The dragon flashes their iridescent scales at the triggering creature to throw off the attack. The dragon gains [[Concealment]] against the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +25 (`pf2:1`) (magical, reach 15 ft., unarmed), **Damage** 3d10+12 piercing"
  - name: "Melee strike"
    desc: "Claws +25 (`pf2:1`) (agile, magical, reach 10 ft.), **Damage** 3d6+12 slashing"
  - name: "Melee strike"
    desc: "Tail +23 (`pf2:1`) (magical, reach 20 ft.), **Damage** 3d8+12 bludgeoning"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 35, attack +27<br>**6th** [[Vibrant Pattern]]<br>**5th** [[Illusory Scene]]<br>**4th** [[Mirage]]<br>**2nd** [[Illusory Creature]], [[Invisibility]], [[Invisibility]] (At Will)<br>**1st** [[Figment]], [[Illusory Object]] (At Will), [[Message]]"
abilities_bot:
  - name: "Captivating Display"
    desc: "`pf2:1` **Frequency** once per 10 minutes <br>  <br> **Effect** The dragon opens the fins on their head, creating a radiant display of enthralling colors. Each creature in a @Template[emanation|distance:30] must succeed at a DC 33 [[Will]] save or be [[Dazzled]] and [[Slowed]] 1 (or [[Slowed]] 2 on a critical failure) for 1 round. Regardless of the result, a creature is then temporarily immune to Captivating Display for 1 minute."
  - name: "Draconic Frenzy"
    desc: "`pf2:2` The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Hallucinatory Breath"
    desc: "`pf2:2` The dragon breathes a cloud that assaults the senses and deals @Damage[12d6[mental]|options:area-damage] damage in a @Template[cone|distance:40] (DC 33 [[Will]] save). A creature that fails its save is also [[Confused]] for 1 round (1 minute on a critical failure) and is then temporarily immune to being confused by Hallucinatory Breath for 1 hour. <br>  <br> The dragon can't use Hallucinatory Breath again for 1d4 rounds."
  - name: "Lunging Bite"
    desc: "`pf2:2` The dragon lunges their head forward, making a jaws Strike with an extended reach of 25 feet."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Mirage dragons are masters of illusion magic and use their powers to deceive others and further their own agendas. In addition to their magical prowess, mirage dragons possess a number of additional features to help them on hunts or mislead attackers, such as their camouflaging scales and a hallucinatory breath that can confound multiple foes at once. Mirage dragons are vain and egotistical figures. They ultimately care more about themselves than others.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

```statblock
creature: "Mirage Dragon (Adult)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
