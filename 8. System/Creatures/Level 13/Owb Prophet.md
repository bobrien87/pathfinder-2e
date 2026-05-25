---
type: creature
group: ["Shadow", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Owb Prophet"
level: "13"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Shadow"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+24; [[Greater Darkvision]]"
languages: "Aklo, Caligni, Common, Sakvroth (cant speak any languages, Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +25, Deception +26, Diplomacy +24, Occultism +23, Religion +25, Stealth +25"
abilityMods: ["+8", "+6", "+8", "+4", "+5", "+7"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Forsaken Patron"
    desc: "Each owb prophet serves as a conduit to one of the shadowy demigods known as the Forsaken. Forsaken patrons are detailed below, and each grants the owb prophet additional abilities. <br>  <br> Each owb prophet gains its power through a connection with a Forsaken patron. The patron grants the owb additional spells and has its own religious symbol and favored weapons. Each entry notes any ability or occult innate spell the Forsaken grants to its prophets, plus its favored weapon. <br>  <br> **Enkaar, the Malformed Prisoner** This mutilated horror is the Forsaken patron of fetters, lethargy, and physical corruption. <br>  <br> - **Spell** [[Phantom Pain]] (4th, at will); <br>  <br> - **Favored Weapon** spiked chain <br>  <br> **Eyes That Watch** This strange trio of feline eyes is the Forsaken patron of inferiority, cats, and strangers. <br>  <br> - **Ability** [[Lifesense]] 120 feet <br>  <br> - **Favored Weapon** dagger <br>  <br> **Grasping Iovett** A beautiful form of indescribable variety, Iovett is the Forsaken patron of accidents, parasites, and reckless lust. <br>  <br> - **Spell** [[Charm]] (4th, at will); <br>  <br> - **Favored Weapon** shortsword <br>  <br> **Husk** This androgynous creature is the Forsaken patron of emptiness, loneliness, and narcissism. <br>  <br> - **Spell** [[Silence]] (4th, at will); <br>  <br> - **Favored Weapon** shortsword <br>  <br> **Lady Razor** This stern magistrate forbids showing kindness or mercy to family members. Lady Razor is the Forsaken patron of family strife, suspicion, and vengeance. <br>  <br> - **Spell** [[Weapon Storm]] (4th, at will); <br>  <br> - **Favored Weapon** dagger <br>  <br> **Reshmit of the Heavy Voice** Taking the form of a massive shadow, Reshmit is the Forsaken patron of broken things, forgetting, and unexpected violence. <br>  <br> - **Spell** [[Rewrite Memory]] (4th, at will); <br>  <br> - **Favored Weapon** morningstar <br>  <br> **Thalaphyrr Martyr-Minder** The Forsaken patron of failed heroics, imprisonment, and squandered time. <br>  <br> - **Spell** [[Slow]] (4th, at will); <br>  <br> - **Favored Weapon** spear"
  - name: "Light Blindness"
    desc: "When first exposed to bright light, the monster is [[Blinded]] until the end of its next turn. After this exposure, light doesn't blind the monster again until after it spends 1 hour in darkness. However, as long as the monster is in an area of bright light, it's [[Dazzled]]."
  - name: "Clutching Cold"
    desc: "A creature hit by the prophet's burning cold Strike becomes [[Immobilized]] in a cluster of binding ice crystals (`act escape dc=31`)."
  - name: "Shadow's Swiftness"
    desc: "An owb prophet can Cast [[Umbral Journey]] as a 3-action activity instead of 1 minute. If they do so, they target only themself."
armorclass:
  - name: AC
    desc: "34; **Fort** +25, **Ref** +23, **Will** +24"
health:
  - name: HP
    desc: "225; **Immunities** cold; **Resistances** mental 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +27 (`pf2:1`) (agile, magical, unarmed, unholy), **Damage** 2d8+11 slashing plus 2d8 cold"
  - name: "Ranged strike"
    desc: "Burning Cold +25 (`pf2:1`) (magical), **Damage** 4d8 cold plus 2d8 cold plus [[Clutching Cold]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 33, attack +25<br>**7th** [[Interplanar Teleport (To or From the Netherworld Only)]]<br>**6th** [[Dominate]]<br>**5th** [[Shadow Blast]], [[Umbral Journey (See Shadow's Swiftness)]]<br>**3rd** [[Mind Reading]] (At Will)<br>**2nd** [[Darkness]] (At Will), [[Invisibility]]<br>**1st** [[Daze]], [[Read Aura]], [[Shield]], [[Void Warp]]"
abilities_bot:
  - name: "Burning Cold Fusillade"
    desc: "`pf2:2` The owb prophet makes three burning cold Strikes."
  - name: "Curse of Darkness"
    desc: "`pf2:1` The owb inflicts a curse on one creature taking persistent cold damage from their burning cold Strike, stealing the victim's vibrancy. The creature must attempt a DC 32 [[Fortitude]] save. <br>  <br> On a failure, the creature gains [[Light Blindness]] and its coloration turns to washed out shades of gray, along with all equipment it carries, wields, or wears. These effects have an unlimited duration. Regardless of the result of its save, the creature is temporarily immune for 1 minute. <br>  <br> If the owb uses this ability on a caligni, the curse can't be removed short of a [[Wish]] ritual or similar powerful magic."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

An owb who comes into contact and is chosen by one of the Forsaken gains a fragment of that demigod's power and forges a permanent connection with it. This act transforms the owb into a larger, more powerful creature and imbues it with the power of divine transference, allowing the owb to gain followers and grant spells to them. These are owb prophets.

Owb prophets may have some portion of the Forsaken's power, but they use their authority to gain more sway over calignis and other worshippers.

These ancient denizens of the Netherworld appear as grayish humanoid torsos covered in translucent funereal veils of shadow. Silent and mysterious, they float about, absent of legs to hold them aloft. Never speaking a word aloud, they instead reach into the minds of nearby creatures to whisper curses, threats, and strange bits of forlorn augury.

These haunting creatures are revered by calignis as proxies of the Forsaken—a strange array of ancestor-like demigods whom many calignis worship. Some even believe owbs are the Forsaken manifested, and that they are able to subtly manipulate creatures on the Netherworld without leaving behind any indication.

A multitude of owbs visit and even remain to advise caligni communities, as varied in personality as the Forsaken. All owbs share a hatred of light and color, except for the flickering glow of the burning cold magic they can hurl as a weapon. Owbs who live among calignis tend to prohibit the use of light and color, using their curse of darkness to quench violators if necessary. The only other similarity across all owbs is their entrenched desire to manipulate their charges through mind-reading and deception, though such manipulation can be either subtle or overt.

```statblock
creature: "Owb Prophet"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
