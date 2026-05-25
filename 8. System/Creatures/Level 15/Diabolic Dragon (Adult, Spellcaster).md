---
type: creature
group: ["Divine", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Diabolic Dragon (Adult, Spellcaster)"
level: "15"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Greater Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Diabolic, Draconic, Pyric, Empyrean, Necril"
skills:
  - name: Skills
    desc: "Acrobatics +27, Athletics +30, Deception +26, Diplomacy +28, Intimidation +26, Religion +26, Society +24, Thievery +27, Hell Lore +24, Legal Lore +26"
abilityMods: ["+8", "+4", "+6", "+3", "+5", "+5"]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair the dragon's vision; they ignore the [[Concealed]] condition from smoke."
  - name: "Diabolic Fire"
    desc: "Any fire damage that a diabolic dragon deals, including fire damage from spells, is imbued with the unholy power of Hell to scorch the spirit as well. A creature takes spirit damage instead of fire damage if that would be more detrimental to the creature (as determined by the GM). A diabolic dragon is immune to the diabolic fire of other diabolic dragons, the fire from divine immolation, and similar effects."
armorclass:
  - name: AC
    desc: "36; **Fort** +29, **Ref** +25, **Will** +26"
health:
  - name: HP
    desc: "285; **Immunities** fire, paralyzed, sleep; **Weaknesses** holy 10"
abilities_mid:
  - name: "+2 Status to All Saves vs. Divine"
    desc: ""
  - name: "Frightful Presence"
    desc: "90 feet. DC 34 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Hell's Sting"
    desc: "`pf2:r` **Trigger** The dragon is critically hit with a melee attack <br>  <br> **Effect** The dragon channels the rancor of Hell back through the body of their foe, overwhelming it with an infernal assault on the mind. The triggering creature takes 8d6 mental damage with a DC 36 [[Will]] save. Holy creatures use an outcome one degree of success worse than they roll on their saving throw."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +30 (`pf2:1`) (fire, magical, reach 15 ft., unarmed, unholy), **Damage** 2d6 fire plus 3d12+11 piercing"
  - name: "Melee strike"
    desc: "Claws +30 (`pf2:1`) (agile, fire, magical, reach 10 ft., unholy), **Damage** 2d6 fire plus 3d8+11 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Tail +28 (`pf2:1`) (fire, magical, reach 20 ft., unholy), **Damage** 3d8+11 bludgeoning plus 2d6 fire plus [[Knockdown]]"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 36, attack +30<br>**6th** (3 slots) [[Banishment]], [[Blessed Boundary]], [[Dominate]]<br>**5th** (3 slots) [[Sending]], [[Translocate]], [[Truespeech]]<br>**4th** (3 slots) [[Dispelling Globe]], [[Divine Wrath]], [[Planar Tether]]<br>**3rd** (3 slots) [[Blindness]], [[Chilling Darkness]], [[Harm]]<br>**2nd** (3 slots) [[Blood Vendetta]], [[Darkness]], [[Translate]]<br>**1st** (3 slots) [[Command]], [[Command]], [[Fear]]<br>**Cantrips** [[Detect Magic]], [[Divine Lance]], [[Message]], [[Sigil]], [[Void Warp]]"
  - name: "Divine Innate Spells"
    desc: "DC 34, attack +26<br>**7th** [[Interplanar Teleport (At Will, Self Only)]]<br>**5th** [[Divine Immolation]]<br>**4th** [[Wall of Fire]] (At Will)<br>**1st** [[Ignition]]"
abilities_bot:
  - name: "Hellfire Breath"
    desc: "`pf2:2` The dragon unleashes a blast of infernal fire that deals @Damage[16d6[fire]|options:area-damage] damage in a @Template[cone|distance:50] (DC 36 [[Reflex]] save). <br>  <br> The dragon can't use Hellfire Breath again for 1d4 rounds."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Hell, according to some theologians, is a living entity in and of itself. Diabolic dragons, these scholars argue, are just extensions of the plane, living creatures that break off from Hell to enact its will. Whether this is true or whether diabolical dragons are simply the reborn souls of dragons sent to Hell, the fact remains that these dragons are powerful, cunning, and tyrannical. Every diabolic dragon's goal is to further Hell's will, though how this happens can vary. Regardless of their goals, these dragons always approach newcomers with an unsettling calmness.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

Draconic Spellcasters
Each dragon features a sidebar on spellcasting dragons of that type. To make a dragon spellcaster, remove the dragon's Draconic Frenzy and Draconic Momentum abilities, and give them the spells outlined in their sidebar. You can swap out any number of these with other spells, provided you keep the same number of spells for each rank. You might also want to increase the dragon's Intelligence, Wisdom, or Charisma modifier by 1 or 2 to reflect their mastery of magic.

```statblock
creature: "Diabolic Dragon (Adult, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
