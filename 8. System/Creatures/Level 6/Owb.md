---
type: creature
group: ["Shadow"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Owb"
level: "6"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Shadow"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Greater Darkvision]]"
languages: "Caligni (cant speak any languages, Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +15, Deception +13, Diplomacy +11, Occultism +12, Religion +11, Stealth +15"
abilityMods: ["+4", "+5", "+4", "+0", "+3", "+3"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Light Blindness"
    desc: "When first exposed to bright light, the monster is [[Blinded]] until the end of its next turn. After this exposure, light doesn't blind the monster again until after it spends 1 hour in darkness. However, as long as the monster is in an area of bright light, it's [[Dazzled]]."
armorclass:
  - name: AC
    desc: "24; **Fort** +14, **Ref** +15, **Will** +13"
health:
  - name: HP
    desc: "90; **Immunities** cold"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +16 (`pf2:1`) (agile, magical, unarmed), **Damage** 1d8+7 slashing plus 1d8 cold"
  - name: "Ranged strike"
    desc: "Burning Cold +17 (`pf2:1`) (magical), **Damage** 2d8 cold plus 1d8 cold"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 23, attack +15<br>**7th** [[Interplanar Teleport (Self Only, To or From the Netherworld Only)]]<br>**5th** [[Shadow Blast]], [[Umbral Journey]]<br>**3rd** [[Mind Reading]] (At Will)<br>**2nd** [[Darkness]] (At Will), [[Invisibility]]<br>**1st** [[Daze]], [[Read Aura]], [[Shield]], [[Void Warp]]"
abilities_bot:
  - name: "Curse of Darkness"
    desc: "`pf2:1` The owb inflicts a curse on one creature taking persistent cold damage from their burning cold Strike, stealing the victim's vibrancy. The creature must attempt a DC 23 [[Fortitude]] save. <br>  <br> On a failure, the creature gains [[Light Blindness]] and its coloration turns to washed out shades of gray, along with all equipment it carries, wields, or wears. These effects have an unlimited duration. Regardless of the result of its save, the creature is temporarily immune for 1 minute. <br>  <br> If the owb uses this ability on a caligni, the curse can't be removed short of a [[Wish]] ritual or similar powerful magic."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Commonly called owbs, or lesser owbs by more powerful owb prophets, most of these mysterious creatures focus on manipulating caligni culture. Among calignis, an owb hides from mortals they deem beneath them-even including calignis in their charge. An owb prefers to select one caligni leader to control from the shadows, manipulating them using charisma and magic. Through coersion of such agents, owbs maintain a steady hand in the politics of the community, either blessing and breaking pacts with other creatures or acting as intermediaries and ambassadors between calignis and powerful external entities.

These ancient denizens of the Netherworld appear as grayish humanoid torsos covered in translucent funereal veils of shadow. Silent and mysterious, they float about, absent of legs to hold them aloft. Never speaking a word aloud, they instead reach into the minds of nearby creatures to whisper curses, threats, and strange bits of forlorn augury.

These haunting creatures are revered by calignis as proxies of the Forsaken—a strange array of ancestor-like demigods whom many calignis worship. Some even believe owbs are the Forsaken manifested, and that they are able to subtly manipulate creatures on the Netherworld without leaving behind any indication.

A multitude of owbs visit and even remain to advise caligni communities, as varied in personality as the Forsaken. All owbs share a hatred of light and color, except for the flickering glow of the burning cold magic they can hurl as a weapon. Owbs who live among calignis tend to prohibit the use of light and color, using their curse of darkness to quench violators if necessary. The only other similarity across all owbs is their entrenched desire to manipulate their charges through mind-reading and deception, though such manipulation can be either subtle or overt.

```statblock
creature: "Owb"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
