---
type: creature
group: ["Angel", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Balisse"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]]"
languages: "Diabolic, Draconic, Empyrean (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +14, Diplomacy +17, Religion +18"
abilityMods: ["+5", "+2", "+4", "+1", "+6", "+5"]
abilities_top:
  - name: "+2 Bonus on Perception to Detect lies and illusions"
    desc: ""
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "26; **Fort** +16, **Ref** +12, **Will** +18"
health:
  - name: HP
    desc: "145; **Weaknesses** unholy 10; **Resistances** fire 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Confessor's Aura"
    desc: "20 feet. <br>  <br> Creatures in the balisse's aura are subject to [[Ring of Truth]] (DC 23 [[Will]] save). Additionally, if these creatures choose to honestly express their own conflicted feelings, the aura makes it easier for them to put words to those feelings."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scimitar +20 (`pf2:1`) (fire, forceful, holy, magical, sweep), **Damage** 2d6+8 slashing plus 1d6 fire"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 26, attack +18<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Divine Wrath]]<br>**3rd** [[Paralyze]]<br>**2nd** [[Cleanse Affliction]], [[Clear Mind]] (At Will), [[Invisibility (At Will) (Self Only)]]<br>**1st** [[Heal]]"
abilities_bot:
  - name: "Brand of the Impenitent"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The balisse marks a creature within their confessor's aura as irredeemable. They can do so only after a failed attempt to convince the creature to repent. The touched creature takes a –1 status penalty to AC and saves, reduces all its resistances by 2, and gains weakness 2 to holy. The duration depends on the target's DC 26 [[Will]] save. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The duration is 1 round. <br> - **Failure** The duration is 1 day. <br> - **Critical Failure** The duration is unlimited. <br>  <br> > [!danger] Effect: Brand of the Impenitent"
  - name: "Guiding Angel"
    desc: "`pf2:1` **Requirements** The balisse is [[Invisible]] <br>  <br> **Effect** The balisse spiritually attaches themself to an adjacent mortal who doesn't have the unholy trait. They merge with the mortal's body and are unable to use any of their spells and abilities other than to interact with the mortal. They can [[Dismiss]] the effect to leave the mortal. While merged, the balisse can either communicate using a bodiless voice only the mortal can hear or can take a form of their choice that only the mortal can see, such as a small angel on the mortal's shoulder."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Balisses, or confessor angels, seek to assist mortals ensnared by moral dilemmas or crises of faith. They prefer to guide people to their own decisions rather than demand obedience to a higher cause, as intrinsic belief is even more powerful than unquestioning obedience. While most balisses are fundamentally honest, they use their guiding angel ability to seem less intimidating and decrease the chance the mortal will simply acquiesce to the opinion of an obviously divine being.

While balisses can spring from any soul with suitable patience and strong counsel, they often form from souls of those who performed evil acts but were redeemed. These souls recognize the struggle and shame of those in similar situations, and can offer advice from the heart rather than from rote sympathy. Many serve the goddess Sarenrae, but they can serve other good deities and empyreal lords as well.

The celestial hosts of angels are messengers and warriors, divided into choirs based on their abilities and purviews. Angels were one of the first creations of the gods, and many still assist their righteous creators throughout the cosmos. Most angels in modern times are not direct creations of the divine, however, instead consisting of ascended mortal souls drawn from the celestial planes.

The majority of unaffiliated angels live in Nirvana, the plane of virtue and enlightenment. Angels who are affiliated with deities dwell in those deities' domains or other areas where that god holds influence. Regardless of residence or service, angels remain benevolent messengers possessed with magical auras to aid their allies.

```statblock
creature: "Balisse"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
