---
type: creature
group: ["Angel", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tabellia"
level: "14"
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
    desc: "+26; [[Darkvision]]"
languages: "Diabolic, Draconic, Empyrean (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +24, Diplomacy +26, Intimidation +28, Religion +24"
abilityMods: ["+8", "+4", "+5", "+4", "+4", "+6"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "36; **Fort** +27, **Ref** +26, **Will** +22"
health:
  - name: HP
    desc: "285; **Weaknesses** unholy 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Messenger's Amnesty"
    desc: "An tabellia with a message to deliver is continually protected by the effect of [[Sanctuary]] (DC 32 [[Will]] save). If the angel breaks the *sanctuary*, the effect returns if the angel ceases hostility for 10 minutes."
  - name: "Traveler's Aura"
    desc: "20 feet. <br>  <br> Creatures in the tabellia's aura are immune to ambient environmental damage from any plane, including severe and extreme heat and cold as well as more otherworldly dangers. The tabellia is never [[Off Guard]] to creatures within their aura."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Holy Warhammer +30 (`pf2:1`) (holy, magical, shove), **Damage** 2d8+14 bludgeoning plus 1d4 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36, attack +28<br>**7th** [[Divine Decree]]<br>**6th** [[Blessed Boundary]]<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Divine Wrath]]<br>**3rd** [[Ring of Truth (At will)]]<br>**2nd** [[Cleanse Affliction]], [[Clear Mind]], [[Invisibility (At Will, Self Only)]]<br>**1st** [[Heal]], [[Light]]"
abilities_bot:
  - name: "Stunning Strike"
    desc: "`pf2:1` **Requirements** The tabellia hit a foe earlier this turn with a weapon Strike <br>  <br> **Effect** The tabellia makes a weapon Strike against the foe. On a success, the foe must also succeed at a DC 34 [[Fortitude]] save or become [[Stunned]] 1 (or [[Stunned]] 2 on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Tabellias are the elite messengers of the celestial realms, serving deities and celestial armies by delivering messages, performing reconnaissance, and providing support for those in need of aid. They watch over planar travelers and take powerful mortals under their wings to mentor them. Tabellias carry scrolls containing important messages and other celestial secrets. Most creatures, even wicked ones, respect the strength of tabellias and allow them to travel untroubled.

Tabellias can form spontaneously from the souls of exceptional mortals but are also sometimes created from such souls intentionally by deities or demigods. In the latter cases, tabellias often bear physical features that mark them as closely affiliated with that deity. A tabellia created by Sarenrae, for example, might have hair made of fire, while one created by Torag might look more dwarven, and one created by Desna could have butterfly wings instead of feathered wings. It's not unusual for tabellias created by deities to share their creators' philosophies and interests.

The celestial hosts of angels are messengers and warriors, divided into choirs based on their abilities and purviews. Angels were one of the first creations of the gods, and many still assist their righteous creators throughout the cosmos. Most angels in modern times are not direct creations of the divine, however, instead consisting of ascended mortal souls drawn from the celestial planes.

The majority of unaffiliated angels live in Nirvana, the plane of virtue and enlightenment. Angels who are affiliated with deities dwell in those deities' domains or other areas where that god holds influence. Regardless of residence or service, angels remain benevolent messengers possessed with magical auras to aid their allies.

```statblock
creature: "Tabellia"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
